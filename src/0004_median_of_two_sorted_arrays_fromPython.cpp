class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int lenA = nums1.size();
        int lenB = nums2.size();
        if (lenA>lenB)
            return findMedianSortedArrays(nums2, nums1);

        int lenAB = lenA + lenB;
        int half = lenAB / 2; // find number of elements in left partition

        int left = 0;
        int right = lenA - 1;
        while (true){
            int Am = (left + right) / 2;
            int Bm = half - Am - 2;
            // std::cout << "left=" << left << " right=" << right << " Am" << Am= << " Bm=" << Bm << std::endl;

            int Aleft = (Am>=0)?nums1[Am]:INT_MIN;
            int Aright = (Am+1<lenA)?nums1[Am+1]:INT_MAX;
            int Bleft = (Bm>=0)?nums2[Bm]:INT_MIN;
            int Bright = (Bm+1<lenB)?nums2[Bm+1]:INT_MAX;

            if ((Aleft <= Bright) && (Bleft <= Aright)) {
                if (lenAB % 2 == 1)
                    return ((double) min(Aright, Bright));
                return ((double) 0.5*(max(Aleft, Bleft) + min(Aright, Bright)));
            }
            if (Aleft > Bright)
                right = Am - 1;
            else
                left = Am + 1;
            if (right < left)
                left = right -1;
        }
        return 0;
    }
};