#include <iostream>
#include <curl/curl.h>
#include <fstream>

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
    std::ifstream ifs("data.json");
    std::string jsonData;
    std::string buff;

    if (!ifs.is_open())
    {
        std::cout << "Impossible to open the file !" << std::endl; 
        return (1);
    }
    else
    {
        while (std::getline(ifs, buff))
        {
            std::cout << "buff =" << buff << "|"<< std::endl;
            if (!jsonData.empty())
                jsonData += "\n";
            jsonData += buff;
        }
    }
    std::cout << jsonData << std::endl;

    return (0);


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
            std::cout << readBuffer << std::endl;
        }

        // Clean up
        curl_slist_free_all(headers);
        curl_easy_cleanup(curl);
    }

    return 0;
}