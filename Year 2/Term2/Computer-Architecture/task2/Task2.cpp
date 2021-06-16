#include <iostream>
#include <ctime>

using namespace std;


int main()
{
    cout << "Task one: " << endl << endl;
       
    srand(time(NULL));

    int const arr_len = 16;
    int arr[arr_len];
    for (int i = 0; i < arr_len; i++) {
        arr[i] = rand() % 100;
    }

    cout << "Initiall array: ";
    for (int i = 0; i < arr_len; i++) {
        cout << arr[i] << " ";
    }

    int n1, n2;
    cout << endl << "Enter 2 array indexes: " << endl;

    bool check = false;
    while (not check) {
        try {
            cin >> n1 >> n2;

            if (!cin) {
                cin.clear();
                cin.ignore(64, '\n');
                throw "Input was not parsable as integer value ";
            }
            else if (n1 > arr_len || n2 > arr_len)
                throw "Index cant be higher than array size";
            else if (n1 < 0 || n2 < 0)
                throw "Index cant be less than 0";
            else
                check = true;
        }
        catch (const char* ex) {
            cout << ex << endl;
        }
    }

    if (n1 > n2) {
        int tmp = n2;
        n2 = n1;
        n1 = tmp;
    }

    for (int i = n1; i <= n2; i++) {
        cout << arr[i] << " ";
    }

    bool sorted = true;
    for (int i = 0; i <= arr_len - 1; i++) {
        if (arr[i] > arr[i + 1])
            continue;
        else
            sorted = false;
            break;
    }

    if (sorted)
        cout << endl << "Array is sorted in descending order" << endl;
    else
        cout << endl << "Array isnt sorted in descending order" << endl;

}