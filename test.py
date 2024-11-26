import requests

# Proxy configuration
PROXY = {
    "http": "http://moviesavingdrive12:ZmuVSycaVu@202.68.184.108:50100",
    "https": "http://moviesavingdrive12:ZmuVSycaVu@202.68.184.108:50100",
}

def resolve_final_url(short_url):
    """
    Resolves a shortened URL to its true final destination using the proxy.
    Tries HTTPS first and falls back to HTTP if SSL issues occur.
    """
    try:
        print(f"Resolving the shortened URL: {short_url} (HTTPS)")
        # Attempt HTTPS resolution first
        response = requests.get(short_url, proxies=PROXY, timeout=10, allow_redirects=True, verify=False)
        print(f"Bypassed URL: {response.url}")
        return response.url
    except requests.exceptions.SSLError as ssl_error:
        print(f"SSL Error encountered: {ssl_error}. Retrying with HTTP...")
        if short_url.startswith("https://"):
            short_url = short_url.replace("https://", "http://")
        try:
            print(f"Resolving the shortened URL: {short_url} (HTTP)")
            response = requests.get(short_url, proxies=PROXY, timeout=10, allow_redirects=True)
            print(f"Bypassed URL: {response.url}")
            return response.url
        except requests.exceptions.RequestException as http_error:
            print(f"HTTP Error encountered: {http_error}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error resolving the URL: {e}")
        return None

def main():
    print("Welcome to the URL Shortener Bypasser")
    print("Enter the shortened URL below. Type 'exit' to quit.")
    
    while True:
        short_url = input("Shortened URL: ").strip()
        
        if short_url.lower() == "exit":
            print("Exiting the bypasser.")
            break
        
        if short_url:
            final_url = resolve_final_url(short_url)
            if final_url:
                print(f"Final URL: {final_url}")
            else:
                print("Could not resolve the URL. Please try again.")

if __name__ == "__main__":
    main()
