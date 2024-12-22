#include <iostream>
#include <string>
#include <vector>
#include <fstream>


inline long long get_next_number(long long number) {
    long long secret = ((number * 64) ^ number) % 16777216;
    secret = ((secret / 32) ^ secret) %  16777216;
    return ((secret * 2048) ^ secret) % 16777216;
}


std::vector<std::vector<int>> generate_sequences() {
    std::vector<std::vector<int>> sequences;

    for (int n1 = 0; n1 < 10; n1++) {
        for (int n2 = 0; n2 < 10; n2++) {
            for (int n3 = 0; n3 < 10; n3++) {
                for (int n4 = 0; n4 < 10; n4++) {
                    for (int n5 = 0; n5 < 10; n5++) {
                        int i1 = n2-n1;
                        int i2 = n3-n2;
                        int i3 = n4-n3;
                        int i4 = n5-n4;

                        std::vector<int> sequence = {i1, i2, i3, i4};
                        sequences.push_back(sequence);
                    }
                }
            }
        }
    }
    
    return sequences;
}


std::vector<int> get_prices_iterations(long long number, int iterations = 2000) {
    std::vector<int> prices = std::vector<int>(2001);
    prices[0] = int(number % 10);

    for (int i = 1; i < iterations+1; i++)
    {   
        number = get_next_number(number);
        prices[i] = int(number % 10);
    }
    
    return prices;
}


int find_first_occurrence_of_sequence(const std::vector<int>& prices, const std::vector<int>& sequence) {
    int i1 = sequence[0];
    int i2 = sequence[1];
    int i3 = sequence[2];
    int i4 = sequence[3];

    for (int i = 4; i < prices.size(); i++)
    {
        int n1 = prices[i-4];
        int n2 = prices[i-3];
        int n3 = prices[i-2];
        int n4 = prices[i-1];
        int n5 = prices[i];

        if (n2-n1 == i1 && n3-n2 == i2 && n4-n3 == i3 && n5-n4 == i4) {
            return n5;
        }
    }
    
    return 0;
}


int main() {
    std::vector<long long> numbers;

    std::ifstream file("day22/input.txt");
    std::string s;
    while(getline(file, s)) {
        numbers.push_back(stoi(s));
    }
    file.close();

    std::vector<std::vector<int>> sequences = generate_sequences();
    std::vector<std::vector<int>> prices_for_numbers = std::vector<std::vector<int>>(numbers.size());
    for (int i = 0; i < numbers.size(); i++)
    {
        prices_for_numbers[i] = get_prices_iterations(numbers[i], 2000);
    }

    int result = 0;
    for (int i = 0; i < sequences.size(); i++) {
        if (i % 1000 == 0) {
            std::cout << i << std::endl;
        }
        std::vector<int> sequence = sequences[i];
        int current_result = 0;

        for (std::vector<int>& prices : prices_for_numbers) {
            current_result += find_first_occurrence_of_sequence(prices, sequence);
        }

        result = std::max(result, current_result);
    }

    std::cout << "The solution to part two is: " << result << std::endl;
}