from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


HOST = "127.0.0.1"
PORT = 8000


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Serving this folder at http://localhost:{PORT} (press Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()
