def https_status(status):
    match status:
        case 200:
            return "OK"
        case 300:
            return "Not Found"
        case 404:
            return "Internal Server Error"
        case _:
            return "Unknown Server Error"

print(https_status(200))