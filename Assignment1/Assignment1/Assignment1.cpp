// Assignment1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

// PROBLEM DEFINITION
// ------------------
// Reverse each word in the input string.
// The order of the words will be unchanged.
// A word is made up of letters and/or numbers.
// Other characters (spaces, punctuation) will not be reversed.


// NOTES
// ------
// Write production quality code
// We prefer clarity over performance (though if you can achieve both - great!)
// You can use the language that best highlights your programming ability
// the template below is in C++
// A working solution is preferred (assert in main() should succeed)
// Bonus points for good tests

#include <iostream>
#include <string>
#include <cassert>
#include <vector>

#if 0

//////////////////////////////////////////////////////////////////////////
// method-1
void reverse_word(std::string& word) 
{
	if (word.length() > 1) {
		std::reverse(word.begin(), word.end());
	}
}

std::string reverse_words(const std::string& str)
{
	std::string result;
	std::string word;

	for (char ch : str) {
		if (std::isalnum(ch)) {
			// build the word
			word += ch;
		}
		else {
			// if a word was being built...
			reverse_word(word);
			result += word + ch;
			word.clear();
		}
	}

	// handle the remain word
	reverse_word(word);
	result += word;

	return result;
}
//////////////////////////////////////////////////////////////////////////

#else

//////////////////////////////////////////////////////////////////////////
// method - 2
std::string reverse_words(const std::string& str) {
	std::string result = str;
	size_t i = 0;

	while (i < result.size()) {
		if (std::isalnum(result[i])) {
			
			size_t start = i;
			while (i < result.size() && std::isalnum(result[i])) {
				++i;
			}
			// Reverse only the word portion
			std::reverse(result.begin() + start, result.begin() + i);
		}
		else {
			++i;
		}
	}

	return result;
}
//////////////////////////////////////////////////////////////////////////

#endif

int main()
{
	std::string test_str = "String; 2be &re*versed...";
	assert(reverse_words(test_str) == "gnirtS; eb2 &er*desrev...");
	return 0;
}