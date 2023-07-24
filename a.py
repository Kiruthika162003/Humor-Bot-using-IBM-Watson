from ibm_watson import AssistantV2
import ibm_cloud_sdk_core

# Initialize Watson Assistant Client
assistant = AssistantV2(
    version='2021-06-14',
    authenticator=ibm_cloud_sdk_core.authenticators.IAMAuthenticator('<your_api_key>')
)
assistant.set_service_url('<service_url>')
assistant_id = '<your_assistant_id>'

def get_humor_response(user_input):
    response = assistant.message(
        assistant_id=assistant_id,
        input={
            'message_type': 'text',
            'text': user_input
        }
    ).get_result()

    # Extract humor response from Watson Assistant's response
    humor_response = response['output']['generic'][0]['text']
    return humor_response

def main():
    print("Humor-Bot: Hello! How can I make you laugh today? (Type 'exit' to end)")

    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            print("Humor-Bot: Goodbye! Have a great day!")
            break

        humor_response = get_humor_response(user_input)
        print("Humor-Bot: " + humor_response)

if __name__ == "__main__":
    main()
