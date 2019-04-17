<?php
	# Sk adib asker, cs490, part 2: beta
 
  $database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");
	
 
	//$id=$_POST['id'];
 
	if(isset($_POST['id'])) $id = $_POST['id'];
	if(isset($_POST['ucid'])) $ucid = $_POST['ucid'];
	if(isset($_POST['result'])) $result = $_POST['result'];
	if(isset($_POST['grade'])) $grade = $_POST['grade'];
  if(isset($_POST['examname'])) $examname = $_POST['examname'];
	if(isset($_POST['topgrade'])) $topgrade = $_POST['topgrade'];
	if(isset($_POST['comments'])) $comments = $_POST['comments'];
 if(isset($_POST['released'])) $released = $_POST['released'];
 if(isset($_POST['testcase'])) $testcase = $_POST['testcase'];
	if(isset($_POST['answer'])) $answer = $_POST['answer'];
  //$testcase = json_encode($testcase);

  #checking weather it is true of false.
	if($id=='')
  {
    #this is a query
		$query= mysqli_query($database, "INSERT INTO `gradedexam` (`ucid`,`examname`,`result`,`testcase`,`answer`,`grade`,`topgrade`,`comments`,`released`)VALUES ('$ucid','$examname','$result','$testcase','$answer','$grade','$topgrade','$comments','$released')");
		
   if(!$query)
		{
			echo "Failed to add grade ";
		}
		else 
		{
       echo "Grade is added ";
			
		}
	}
 
	else
  {
    #this is a query
		$query= mysqli_query($database, "UPDATE `gradedexam` set `ucid`='$ucid',`examname`='$examname', `result`='$result',`testcase`='$testcase',`answer`='$answer',`grade`='$grade' `topgrade`='$topgrade',`comments`='$comments',`released`='$released', where `id`='$id' ");
		
    if ($query) 
		{
			echo "Grade is updated ";
		}
		else 
		{
			echo "Grade did not update ";
		}
	}
 
 
?>