import requests
import time
import json

API_VERSIONS = ["v9", "v10"]
ENDPOINT = "/users/@me"
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

headers_template = {
    "Authorization": f"Bot {BOT_TOKEN}",
    "Content-Type": "application/json",
}

def test_discord_versions():
    results = []
    for version in API_VERSIONS:
        url = f"https://discord.com/api/{version}{ENDPOINT}"
        print(f"[⏳] Requesting: {url}")

        start = time.time()
        try:
            response = requests.get(url, headers=headers_template)
            elapsed = round((time.time() - start) * 1000, 2)
        except Exception as e:
            print(f"[❌] Error on version {version}: {e}")
            continue

        result = {
            "version": version,
            "status_code": response.status_code,
            "elapsed_ms": elapsed,
            "rate_limit_remaining": response.headers.get("X-RateLimit-Remaining"),
            "rate_limit_reset_after": response.headers.get("X-RateLimit-Reset-After"),
            "retry_after": response.headers.get("Retry-After")
        }

        try:
            result["response"] = response.json()
        except Exception:
            result["response"] = response.text

        results.append(result)

    with open("output/result_v9_v10.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print("\n[✅] API 테스트 완료. 결과는 'output/result_v9_v10.json'에 저장됨.")
    return results


if __name__ == "__main__":
    test_discord_versions()
