
<?php
  # Sk adib asker, cs490
  $database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");
	
  if(isset($_POST['topic'])) $topic = $_POST['topic'];
  if(isset($_POST['difficulty'])) $difficulty = $_POST['difficulty'];
  
	
  if($difficulty == "any" and $topic=="any")
  {
 
  $sql = mysqli_query($database, "SELECT * FROM questionbank ");
  while($result= mysqli_fetch_assoc($sql))
  {  
  

   $data[]=array("id"=>$result['id'],"topic"=>$result['topic'],"difficulty"=>$result['difficulty'], "question"=>$result['question'], "testcase"=>$result['testcase']);
   
  }
   
  echo json_encode($data);
  }
  elseif($difficulty == "any")
  {
 
  $sql = mysqli_query($database, "SELECT * FROM questionbank WHERE topic like '$topic'");
  while($result= mysqli_fetch_assoc($sql))
  {  
  

   $data[]=array("id"=>$result['id'],"topic"=>$result['topic'],"difficulty"=>$result['difficulty'], "question"=>$result['question'], "testcase"=>$result['testcase']);
   
  }
   
  echo json_encode($data);
  }
  elseif($topic == "any")
  {
 
  $sql = mysqli_query($database, "SELECT * FROM questionbank WHERE difficulty like '$difficulty' ");
  while($result= mysqli_fetch_assoc($sql))
  {  
  

   $data[]=array("id"=>$result['id'],"topic"=>$result['topic'],"difficulty"=>$result['difficulty'], "question"=>$result['question'], "testcase"=>$result['testcase']);
   
  }
   
  echo json_encode($data);
  }
  else
  {
  $sql = mysqli_query($database, "SELECT * FROM questionbank WHERE topic like '$topic' and difficulty like '$difficulty' ");

  while($result= mysqli_fetch_assoc($sql))
  {  
  
   $data[]=array("id"=>$result['id'],"topic"=>$result['topic'],"difficulty"=>$result['difficulty'], "question"=>$result['question'], "testcase"=>$result['testcase']);
   
  }
  echo json_encode($data);
 
  }
  

?>


