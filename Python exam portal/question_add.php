<?php
	# Sk adib asker, cs490, part 2: beta
 
  $database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");
	
 
	$id=$_POST['id'];
 
	if(isset($_POST['topic'])) $topic = $_POST['topic'];
	if(isset($_POST['difficulty'])) $difficulty = $_POST['difficulty'];
	if(isset($_POST['question'])) $question = $_POST['question'];
	if(isset($_POST['testcase'])) $testcase = $_POST['testcase'];
  $testcase = json_encode($testcase);

  #checking weather it is true of false.
	if($id=='')
  {
    #this is a query
		$query= mysqli_query($database, "INSERT INTO `questionbank` (`topic`,`difficulty`,`question`,`testcase`)VALUES ('$topic','$difficulty','$question','$testcase')");
		
   if(!$query)
		{
			echo "Failed to add question to the question bank.";
		}
		else 
		{
       echo "Question is added to the question bank.";
			
		}
	}
 
	else
  {
    #this is a query
		$query= mysqli_query($database, "UPDATE `questionbank` set `topic`='$topic', `difficulty`='$difficulty',`question`='$question', `testcase`='$testcase', where `id`='$id' ");
		
    if ($query) 
		{
			echo "Question is updated";
		}
		else 
		{
			echo "Question did not update";
		}
	}
 
 
?>