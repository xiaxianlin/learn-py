status_code = int(input("响应状态码: "))
match status_code:
    case 400 | 405:
        description = "Invalid Request"
    case 401 | 403 | 404:
        description = "Not Allowed"
    case _:
        description = "Unknown Status Code"
print("状态码描述:", description)
