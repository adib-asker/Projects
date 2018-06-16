<html>
  <head>
      <title>Stocks Page</title>
  </head>

  <body>

<?php
  $conn = mysqli_connect("localhost", "root", "mysql");
  if (!$conn) {
    die(mysqli_connect_error());
    echo "connection error";
  }

  $selectdb = mysqli_select_db($conn, "ucid");

  $columns = array('id', 'issue', 'volume', 'price', 'diff');

  $sortBy = (isset($_GET['SortBy'])) ? $_GET['SortBy'] : 'id';
  if(in_array($sortBy, $columns) == FALSE){
    $sortBy = 'id';
  }


  $result = mysqli_query($conn, "SELECT * from stocks ORDER BY $sortBy");
  $num    = mysqli_num_rows ($result);
?>

  <table border="1" cellspacing="0" cellpadding="0" width="100%">
    <tr>
      <th><a href="?SortBy=id">ID</a></th>
      <th><a href="?SortBy=issue">Issue</a></th>
      <th><a href="?SortBy=volume">Volume</a></th>
      <th><a href="?SortBy=price">Price</a></th>
      <th><a href="?SortBy=diff">Diff</a></th>
      <th><a href="?SortBy=percent">Percent</a></th>
    </tr>

<?php
  for ($i=0; $i < $num; $i++){
      $row = mysqli_fetch_row($result);

     echo "<tr>
       <td class=\"num\">$row[0]</td>
       <td style=\"max-width:307px\">$row[1]</td>
       <td style=\"font-weight:bold;\" align=\"right\">$row[2]</td>
       <td >$row[3]</td>
       <td>$row[4]</td>
       <td style=\"border-right:0px\">$row[5]</td>
     </tr>";
  }

  mysqli_close($conn);
?>
  </table>
  </body>
</html>
