/* 
Problem: 

On some old cellphones, there was not enough room for a complete keyboard and users had to use their keypad with 9 numbers to type out text. 
Each number corresponded to several possible characters. For example, typing ‘2’ could mean either ‘a’, ‘b’, or ‘c’. If a user wanted to type out “cat” they would type 228, but 228 could also mean “act” or “bat”.
Question: Given an input string of digits and a text file containing a list of all valid words, your goal is to produce a vector of possible, valid words in alphabetical order for the given string of digits. Please also leave a short description about the run time complexity of your algorithm.
We have provided you with the following to help get you started. Feel free to modify however you want.
A mapping from each number to its possible characters.
A file containing a list of valid words and some starter code to open this file and read it into a vector.
Some example test cases.
*/

Question: Given an input string of digits and a text file containing a list of all valid words, your goal is to produce a vector of possible, valid words in alphabetical order for the given string of digits. Please also leave a short description about the run time complexity of your algorithm.

We have provided you with the following to help get you started. Feel free to modify however you want.

A mapping from each number to its possible characters.
A file containing a list of valid words and some starter code to open this file and read it into a vector.
Some example test cases.
Please do this question in c++. You may use the standard library and the catch test framework, but please don’t use other third-party libraries. We also expect a solution that is uniquely yours. Looking up resources is fine, but looking up solutions is no fun. Feel free to handle edge cases/error handling however you feel is most appropriate.

#include <algorithm>
#include <cstddef>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <vector>

#define CATCH_CONFIG_MAIN
#include "catch.hpp"

using namespace std;

// Feel free to modify any of this starter code however you want. 
static const unordered_map<int, vector<char>> kT9Mapping{{2, {'a', 'b', 'c'}},
                                                         {3, {'d', 'e', 'f'}},
                                                         {4, {'g', 'h', 'i'}},
                                                         {5, {'j', 'k', 'l'}},
                                                         {6, {'m', 'n', 'o'}},
                                                         {7, {'p', 'q', 'r', 's'}},
                                                         {8, {'t', 'u', 'v'}},
                                                         {9, {'w', 'x', 'y', 'z'}}};

// charToKeyT9Mapping is the inverse of kT9Mapping (maps the char to the number)
unordered_map<char, int> charToKeyT9Mapping {
  {'a', 2},
  {'b', 2},
  {'c', 2},
  {'d', 3},
  {'e', 3},
  {'f', 3},
  {'g', 4},
  {'h', 4},
  {'i', 4},
  {'j', 5},
  {'k', 5},
  {'l', 5},
  {'m', 6},
  {'n', 6},
  {'o', 6},
  {'p', 7},
  {'q', 7},
  {'r', 7},
  {'s', 7},
  {'t', 8},
  {'u', 8},
  {'v', 8},
  {'w', 9},
  {'x', 9},
  {'y', 9},
  {'z', 9},
};

const int NUM_CHILDREN = 8;
// TrieNode stores an array of children TrieNodes and vector of matching words
struct TrieNode {
  struct TrieNode *children[NUM_CHILDREN];
  bool isWord;
  vector<string> words;
};

// create a new TrieNode with default values
struct TrieNode *makeTrieNode() {
  struct TrieNode *newNode = new TrieNode;
  newNode->isWord = false;

  for (int i = 0; i < NUM_CHILDREN; i++) {
    newNode->children[i] = nullptr;
  }
  return newNode;
}

// insert a word into the given Trie
void insert(struct TrieNode *root, string key) {
  struct TrieNode *currNode = root;

  for (auto c : key) {
    int index = charToKeyT9Mapping[c] - 2;
    if (!currNode->children[index]) {
      currNode->children[index] = makeTrieNode();
    }
    currNode = currNode->children[index];
  }

  currNode->isWord = true;
  currNode->words.push_back(key);
}

// traverse the Trie to find the matching words for the given number
vector<string> search(struct TrieNode *root, string key) {
  struct TrieNode *currNode = root;
  vector<string> possibleWords;

  for (auto c : key) {
    int index = c - '2';
    // error checking index
    if (index < 0 || index > 7 || !currNode->children[index]) {
      possibleWords.push_back("No matching valid words found");
      return possibleWords;
    }
    currNode = currNode->children[index];
  }

  if (currNode->isWord == true) {
    possibleWords = currNode->words;
  } else {
    possibleWords.push_back("No matching valid words found");
  }
  return possibleWords;
}

struct TrieNode *validWordsTrie = makeTrieNode();

vector<string> ReadWords() {
  vector<string> valid_words;
  ifstream word_file("/home/coderpad/data/words.txt");
  if (word_file.is_open()) {
    string word;
    while (getline(word_file, word)) {
      valid_words.push_back(word);
      insert(validWordsTrie, word); // inserting words into the trie as they're read in
    }
    word_file.close();
  }
  return valid_words;
}

vector<string> GetPossibleWords(const string& number_string) {
  vector<string> possible_words = search(validWordsTrie, number_string);
  sort(possible_words.begin(), possible_words.end());
  return possible_words;
}

bool PossibleWordsMatch(const vector<string>& expected, const vector<string>& computed) {
  return expected == computed;
}

/* Please briefly describe the run time of your solution below:
 *
 * Time Complexity for search & insert: O(key_length)
 * Space Complexity: O(num_children * max_key_length * num_keys) where num_children = 8
 *
 * Description of my Solution:
 * 
 * I used a trie to store all the valid words from the provided file as they were being
 * read in the ReadWords() function. This was done using the insert() function.
 * Then, whenever GetPossibleWords(number_string) is called, I used the
 * search(number_string) function to either return the possible valid words in
 * alphabetical order or "No matching valid words found".
 *
 */

TEST_CASE("Possible words match", "[GetPossibleWords]") {
  const auto word_list = ReadWords();
  
  // Build your data structure to hold the valid words here and then pass it to GetPossibleWords.
  REQUIRE(PossibleWordsMatch({"act", "bat", "cat"}, GetPossibleWords("228")));
  REQUIRE(PossibleWordsMatch({"kodiak"}, GetPossibleWords("563425")));
  // Add your test cases here.
  // Invalid Cases:
  REQUIRE(PossibleWordsMatch({"No matching valid words found"}, GetPossibleWords("2")));
  REQUIRE(PossibleWordsMatch({"No matching valid words found"}, GetPossibleWords("")));
  REQUIRE(PossibleWordsMatch({"No matching valid words found"}, GetPossibleWords("23456789")));
  // Valid Cases:
  REQUIRE(PossibleWordsMatch({"robot"}, GetPossibleWords("76268")));
  REQUIRE(PossibleWordsMatch({"random"}, GetPossibleWords("726366")));
  REQUIRE(PossibleWordsMatch({"mane", "name", "oboe"}, GetPossibleWords("6263")));
  REQUIRE(PossibleWordsMatch({"java", "kata", "kava", "lava"}, GetPossibleWords("5282")));
  REQUIRE(PossibleWordsMatch({"pat", "qat", "rat", "sat", "sau"}, GetPossibleWords("728")));
}
