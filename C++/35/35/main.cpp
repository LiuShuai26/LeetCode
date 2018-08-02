//
//  main.cpp
//  35
//
//  Created by Shuai Liu on 8/2/18.
//  Copyright © 2018 Shuai Liu. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

int searchInsert(vector<int>& nums, int target) {
    int low = 0, high = nums.size()-1;
    
    while (low <= high) {
        int mid = low + (high-low)/2;
        if (nums[mid] < target)
            low = mid+1;
        else
            high = mid-1;
    }
    return low;
}

int main(int argc, const char * argv[]) {
    vector<int> array(5);
    array = {1, 3, 4, 6};
    int answer = searchInsert(array, 5);
    cout << answer << endl;
    return 0;
};
