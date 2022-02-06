#include <iostream>
#include <windows.h>

using namespace std;


struct bin_arr {
	int arr[8];
};


int bin_to_dec(int arr[], int size) {
	int n = 0;
	for (int i = 0; i < size; i++)
		n = n * 2 + arr[i];

	return n;
}


bin_arr dec_to_bin(int n) {
	bin_arr b;
	int b_size = sizeof(b.arr) / sizeof(b.arr[0]);

	for (int i = 0; i < 8; i++)
		b.arr[i] = 0;

	for (int i = b_size - 1; n > 0; i--) {
		b.arr[i] = n % 2;
		n = n / 2;
	}

	return b;
}


bin_arr shift(bin_arr b, int b_size) {
	const int temp = b.arr[b_size - 1];
	for (int i = b_size - 1; i > 0; i--)
		if (i != 1)
			b.arr[i] = b.arr[i - 1];
		else
			b.arr[i + 1] = b.arr[i - 1];
	b.arr[0] = temp;

	return b;
}



int main() {

	cout << "Task two: " << endl;

	int n;
	cout << endl << "Enter byte value in decimals:  " << endl;
	cin >> n;
	if (n > 255)
		n %= 256;
	else if (!cin)
		n = 100;

	bin_arr b = dec_to_bin(n);
	const int b_size = sizeof(b.arr) / sizeof(b.arr[0]);
	cout << "Decimal num: " << n << endl;
	cout << "Binary num: ";
	for (int i = 0; i < b_size; i++) {
		if (i == 1) {
			SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 4);
			cout << b.arr[i];
			SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 7);
		}
		else
			cout << b.arr[i];
	}

	bin_arr b_shifted = shift(b, b_size);
	cout << endl << endl << "Shifted binary num: ";
	for (int i = 0; i < b_size; i++) {
		if (i == 1) {
			SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 4);
			cout << b_shifted.arr[i];
			SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 7);
		}
		else
			cout << b_shifted.arr[i];
	}
	int n_shifted = bin_to_dec(b_shifted.arr, b_size);
	cout << endl << "Shifted decimal num: " << n_shifted << endl;
	
	n_shifted *= 2;
	b_shifted = dec_to_bin(n_shifted);
	cout << endl << endl << "Shifted binary num * 2: ";
	for (int i = 0; i < b_size; i++) 
		cout << b_shifted.arr[i];
	cout << endl << "Shifted decimal num: * 2: " << n_shifted << endl;

}