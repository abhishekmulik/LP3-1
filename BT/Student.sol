pragma solidity ^0.8.0;
contract StudentData{
    struct Student{
        int roll;
        string name;
    }
    event Log(string s);

    Student[] record;
    function addStudent(string memory name,int rollno) public{
        record.push(Student(rollno,name));
    } 
    function showRecord() public view returns(Student[] memory){
        return record;
    }

    fallback() external payable{
        emit Log("Money recieved");
         
    }

}
