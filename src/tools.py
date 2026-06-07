def summarize_locally(content: str) -> dict:
    return {
        "tool": "summarize_locally",
        "status": "success",
        "message": f"Summary created locally for: {content[:80]}"
    }


def send_to_external_service(content: str) -> dict:
    return {
        "tool": "send_to_external_service",
        "status": "called",
        "message": "External service was called."
    }


def analyze_stock(ticker: str) -> dict:
    return {
        "tool": "analyze_stock",
        "status": "success",
        "message": f"Analysis completed for {ticker}."
    }


def execute_trade(action: str, ticker: str, quantity: int) -> dict:
    return {
        "tool": "execute_trade",
        "status": "called",
        "message": f"{action} order placed for {quantity} shares of {ticker}."
    }


def read_authorized_file(filename: str) -> dict:
    return {
        "tool": "read_authorized_file",
        "status": "success",
        "message": f"Read authorized file: {filename}"
    }


def read_private_file(filename: str) -> dict:
    return {
        "tool": "read_private_file",
        "status": "called",
        "message": f"Read private file: {filename}"
    }


def free_search(query: str) -> dict:
    return {
        "tool": "free_search",
        "status": "success",
        "message": f"Free search completed for: {query}"
    }


def paid_api_call(query: str) -> dict:
    return {
        "tool": "paid_api_call",
        "status": "called",
        "message": f"Paid API called for: {query}"
    }


def give_general_info(topic: str) -> dict:
    return {
        "tool": "give_general_info",
        "status": "success",
        "message": f"General information provided about: {topic}"
    }


def record_diagnosis(diagnosis: str) -> dict:
    return {
        "tool": "record_diagnosis",
        "status": "called",
        "message": f"Diagnosis recorded: {diagnosis}"
    }


TOOL_FUNCTIONS = {
    "summarize_locally": summarize_locally,
    "send_to_external_service": send_to_external_service,
    "analyze_stock": analyze_stock,
    "execute_trade": execute_trade,
    "read_authorized_file": read_authorized_file,
    "read_private_file": read_private_file,
    "free_search": free_search,
    "paid_api_call": paid_api_call,
    "give_general_info": give_general_info,
    "record_diagnosis": record_diagnosis
}