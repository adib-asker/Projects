<?php
  # Sk adib asker, cs490, part 2: beta

  $database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");
	
	if(isset($_POST['id'])) $id = $_POST['id'];
 if(isset($_POST['examname'])) $examname = $_POST['examname'];
// $name = $_POST['name'];
if(isset($_POST['points'])) $points = $_POST['points'];

 if(isset($_POST['question'])) $question = $_POST['question'];
 if(isset($_POST['testcase'])) $testcase = $_POST['testcase'];
 //$examname="test4";
//$query= mysqli_query($database, "INSERT INTO `exam`(`examname`) VALUES ('$examname')");
 
 //$points="50";
  //$examname="testname";

  $query= mysqli_query($database,"INSERT INTO exam(points,examname,question,testcase) SELECT '$points','$examname',question,testcase FROM `questionbank` WHERE `id` = '$id'");
 
 #checking weather the exam has added or not
	if(!$query)
 {
   echo "Exam Table have not been added ";
  	
 }
 
	else 
  {
  echo "Exam Table have been added successfuly ";
  }
?>