#include "Master.hpp"

// This function will be used to collect the response from the API request
size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

int main() {
    // Your OpenAI API key
    std::string apiKey = "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";
    
    // API URL for OpenAI GPT-3 (or GPT-4)
    std::string url = "https://api.openai.com/v1/chat/completions";
    
    // JSON data to send in the POST request
    std::string jsonData = read_json_to_string("data.json");

    // Initialize curl
    CURL* curl = curl_easy_init();
    if(curl) {
        CURLcode res;
        std::string readBuffer;

        // Set the request URL
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());

        // Set the HTTP headers (including Authorization with your API Key)
        struct curl_slist* headers = NULL;
        headers = curl_slist_append(headers, "Content-Type: application/json");
        headers = curl_slist_append(headers, ("Authorization: Bearer " + apiKey).c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        // Set the request body (the JSON data)
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, jsonData.c_str());

        // Set the callback function to capture the response data
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

        // Make the request
        res = curl_easy_perform(curl);

        // Check for errors
        if(res != CURLE_OK) {
            std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
        } else {
            // Print the response
            std::cout << "Response from OpenAI API: " << std::endl;
            write_txt("response.json", readBuffer);
            // get_json("response.json");
        }

        // Clean up
        curl_slist_free_all(headers);
        curl_easy_cleanup(curl);
    }

    return 0;
}