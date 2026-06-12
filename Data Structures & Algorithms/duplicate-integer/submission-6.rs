use std::collections::HashMap as HM2;
impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut seens:HM2<i32,i8> = HM2::new();
        for num in nums {
            if seens.contains_key(&num){
                return true
            } else {
                seens.insert(num,1 as i8);
            }
        }
        return false
    }
}
