from ollama import chat


# =========================
# Traffic Light Functions
# =========================

def pedestrian_crossing():
    print("\n🚦 الإشارة: 🔴 أحمر للعربيات")
    print("🚶 المشاة: يمكنهم العبور\n")
    return "تم تفعيل إشارة عبور المشاة: الأحمر للعربيات والمشاة يمكنهم العبور."


def vehicle_crossing():
    print("\n🚦 الإشارة: 🟢 أخضر للعربيات")
    print("🚗 العربيات: يمكنها العبور\n")
    return "تم تفعيل إشارة عبور العربيات: الأخضر للعربيات."


def traffic_status():
    print("\n🚦 حالة الإشارة الحالية")
    print("🔴 أحمر للعربيات")
    print("🚶 المشاة يمكنهم العبور\n")
    return "حالة الإشارة الحالية: أحمر للعربيات والمشاة يمكنهم العبور."


# =========================
# Tools available to the AI
# =========================

tools = [
    {
        "type": "function",
        "function": {
            "name": "pedestrian_crossing",
            "description": "تشغيل إشارة عبور المشاة عندما يكون المستخدم شخصًا ماشيًا على قدميه ويريد عبور الشارع.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "vehicle_crossing",
            "description": "تشغيل إشارة عبور السيارات عندما يكون المستخدم يقود سيارة ويريد عبور الشارع.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "traffic_status",
            "description": "معرفة حالة إشارة المرور الحالية.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
]


# =========================
# System instructions
# =========================

messages = [
    {
        "role": "system",
        "content": """
أنت نظام ذكي للتحكم في إشارة مرور.

تحدث مع المستخدم باللغة العربية.

افهم طلب المستخدم من كلامه الطبيعي ولا تطلب منه اسم أي function.

إذا كان المستخدم مشاة ويريد عبور الشارع استخدم pedestrian_crossing.

إذا كان المستخدم يقود سيارة ويريد عبور الشارع استخدم vehicle_crossing.

إذا كان المستخدم يسأل عن حالة إشارة المرور الحالية استخدم traffic_status.

إذا كانت المعلومات غير كافية، لا تخمن.
اسأل المستخدم سؤالًا توضيحيًا.

استخدم الـfunctions عندما يكون تنفيذها مناسبًا.
""",
    }
]


# =========================
# Chat loop
# =========================

while True:

    user_input = input("\nأنت: ")

    if user_input.lower() in ["exit", "quit", "خروج"]:
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = chat(
        model="qwen3:8b",
        messages=messages,
        tools=tools
    )

    messages.append(response.message)

    # Check if AI wants to call a function
    if response.message.tool_calls:

        for tool_call in response.message.tool_calls:

            function_name = tool_call.function.name

            if function_name == "pedestrian_crossing":
                result = pedestrian_crossing()

            elif function_name == "vehicle_crossing":
                result = vehicle_crossing()

            elif function_name == "traffic_status":
                result = traffic_status()

            else:
                result = "Function غير معروفة."

            messages.append({
                "role": "tool",
                "content": result
            })

        # Send function result back to AI
        final_response = chat(
            model="qwen3:8b",
            messages=messages,
            tools=tools
        )

        messages.append(final_response.message)

        print("AI:", final_response.message.content)

    else:
        print("AI:", response.message.content)