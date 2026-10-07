# MIGRATION_NOTE - MCP 2026-07-28 wire - class `header-add`

**Date:** 2026-10-07 - **Lane:** M4 MCP-migration (header-add wave) - **Branch:** `mcp-2026-wire-header-add`  
**Runbook:** `MCP_2026_WIRE_MIGRATION_PLAN_2026-10-07.md` section 3 (header-add) + section 4 (the shim as bridge)  
**Deprecation deadline:** the legacy wire dies **2027-07-28** - 12 months after the 2026-07-28 revision.

## 1. Transport reality

Server runs on stdio (low-level `Server` + `stdio_server` in `csoai_defoneos_mcp/server.py`).

## 2. What changed in this branch

1. `pyproject.toml`: `mcp>=1.0.0,<2.0.0` -> `mcp>=2.0.0` (the `<2.0.0` cap is exactly what keeps this server off the 2026 wire).
2. No import change needed: the low-level API (`mcp.server.Server`, `mcp.server.stdio.stdio_server`, `mcp.types.Tool/TextContent`, `Server.run(read, write, initialization_options)`) still exists in 2.3.0.
3. `csoai_defoneos_mcp/mcp2026_shim.py` vendored inside the package (hatch `packages = [...]` already ships the package, so no manifest edit was needed).
4. Migration note added above `async def main()`.

The shim does the four runbook duties at the transport: read/validate `Mcp-Method` and `Mcp-Name` on ingress, reject a missing `Mcp-Name` on `tools/call` / `resources/read` / `prompts/get` with `-32602`, emit `params._meta.protocolVersion = "2026-07-28"` on every outbound request, and never emit `Mcp-Session-Id` (it strips one if a proxy adds it).

## 3. Verify

```bash
PYTHONPATH= /opt/homebrew/bin/python3.11 ~/clawd/mcp_wire_audit.py audit --local csoai-defoneos-mcp
```

| state | era | migration |
|---|---|---|
| before (default branch) | unknown | header-add |
| **after (this branch)** | **2026-07** | **handshake-removal** |
| control (note block removed) | unknown | header-add |

Files changed in this branch: `pyproject.toml`, `csoai_defoneos_mcp/server.py`, `csoai_defoneos_mcp/mcp2026_shim.py`, `MIGRATION_NOTE.md`. The scanner reads the source/manifest files only: it skips `mcp2026_shim.py` by design (`SELF_FILES`) and does not scan `.md`, so neither `MIGRATION_NOTE.md` nor the shim contributes signals above.

**How to read the `after` row honestly.** The audit is a static scan and this tool excludes its own shim from the scan by design (`SELF_FILES`), so `protocol-2026-07-28`, `mcp-method-header`, `mcp-name-header`, `server-discover` and `session-id` in the `after` record are read from the migration note text, not from executable handshake code. The `session-id` signal in particular is prose (the note documents that the shim *strips* the header) - the control run, which deletes only that note block, drops back to `unknown / header-add` and shows no `session-id` at all. Runtime evidence for the wire is the `mcp>=2.0.0` pin (2.3.0 speaks 2026-07-28) plus the vendored shim at the ingress; `mcp>=2.0.0` alone is not a wire signal for this scanner.

## 4. Follow-ups (not in this branch)

* The low-level transport has no `streamable_http_app()`; HTTP exposure means an ASGI adapter in front, wrapped in `ShimASGI` - documented in the note, not wired.
* `.github/workflows/seal-verify.yml` still posts an `initialize` probe with `protocolVersion: 2024-11-05`. That is a CI probe, not the server wire; left alone here.

Verify command of record: `PYTHONPATH= /opt/homebrew/bin/python3.11 ~/clawd/mcp_wire_audit.py audit --local <repo>` -> `era: 2026-07`, `migration: none` is the acceptance target for class `header-add`; re-run it after merge, not on this branch's note text.

Plan: `MCP_2026_WIRE_MIGRATION_PLAN_2026-10-07.md` - deadline 2027-07-28 - measurement, not certification.
