#include "reverse_string.h"

namespace reverse_string {

// TODO: add your solution here
    std::string reverse_string(std::string word){
        std::string reversedString{""};
        for(int i=word.length()-1;i>=0;i--){
            reversedString+=word[i];
        }
        return reversedString;
    }

}  // namespace reverse_string
