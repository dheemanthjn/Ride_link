from client.api import ping_server

def main():
    print("🚖 Mini-Uber Client 🚖")
    print("Sending ping request to server...")

    try:
        result = ping_server()
        print("✅ Server Response:", result)
    except Exception as e:
        print("❌ Error communicating with server:", e)

if __name__ == "__main__":
    main()
