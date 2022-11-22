pragma solidity 0.4.25;

contract Bank{
    int bal;
    constructor() public{
        bal=0;
    }
    function depositMoney(int amt)public{
        bal=bal+amt;
    }
    function withdrawMoney(int amt) public{
        require(amt <= bal,"Cant withdraw Money more than that of the balance");
        bal=bal-amt;
    }
    function showBalance() view public returns(int){
        int temp = bal;
        return temp;
    }
}
