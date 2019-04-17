<?php
  # Sk adib asker, cs490, part 2: beta

  $database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");
	$examname = "dontdelete";
	//if(isset($_POST['id'])) $id = $_POST['id'];
if(isset($_POST['examname'])) $examname = $_POST['examname'];
// $name = $_POST['name'];
//f(isset($_POST['points'])) $points = $_POST['points'];

 if(isset($_POST['question'])) $question = $_POST['question'];
 if(isset($_POST['testcase'])) $testcase = $_POST['testcase'];
 //$examname="test4";
//$query= mysqli_query($database, "INSERT INTO `exam`(`examname`) VALUES ('$examname')");
 
 //$points="50";
  //$examname="testname";

  $query= mysqli_query($database,"DELETE FROM `exam` WHERE `examname` = '$examname'");
 
 #checking weather the exam has added or not
	if(!$query)
 {
   echo "Exam has not been deleted ";
  	
 }
 
	else 
  {
  echo "Exam has been deleted successfuly ";
  }
?>