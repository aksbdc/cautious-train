// Generated by Wrangler by running `wrangler --experimental-json-config types ./src/server/worker-configuration.d.ts`

interface Env {
	Chat: DurableObjectNamespace<import("./index").Chat>;
	ASSETS: Fetcher;
}
