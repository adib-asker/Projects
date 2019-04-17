<?php
    
    $weather = "";
    $error = "";
    
    if (array_key_exists('city', $_GET)) {
        
        $city = str_replace(' ', '', $_GET['city']);
        
        $file_headers = @get_headers("http://www.weather-forecast.com/locations/".$city."/forecasts/latest");
        
        
        if($file_headers[0] == 'HTTP/1.1 404 Not Found') {
    
            $error = "That city could not be found....";

        } else {
        
        $forecastPage = file_GET_contents("https://www.weather-forecast.com/locations/".$city."/forecasts/latest");
       # echo $forecastPage;
      $pageArray = explode('<p class="b-forecast__table-description-content"><span class="phrase">', $forecastPage);
           
        
        
        if (sizeof($pageArray) > 1) {
        
                $secondPageArray = explode('</span>', $pageArray[1]);
            
                if (sizeof($secondPageArray) > 1) {

                    $weather = $secondPageArray[0];
                    
                } else {
                    
                    $error = "That city could not be found....";
                    
                }
            
            } else {
            
                $error = "That city could not be found.";
            
            }
            
            
        
        }
        
    }


?>


<!DOCTYPE html>
<html lang="en">
  <head>
    

      <title>Weather Scraper</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/css/bootstrap.min.css" integrity="sha384-y3tfxAZXuh4HwSYylfB+J125MxIs6mR5FOHamPBG064zB+AFeWH94NdvaCBm8qnd" crossorigin="anonymous">
      
      <style type="text/css">
      
      html { 
          background: url(background.jpg) no-repeat center center fixed; 
          -webkit-background-size: cover;
          -moz-background-size: cover;
          -o-background-size: cover;
          background-size: cover;
          }
        
          body {
              
              background: none;
              
          }
          
          .container {
              
              text-align: center;
              margin-top: 100px;
              width: 450px;
              
          }
          
          input {
              
              margin: 20px 0;
              
          }
          
          #weather {
              
              margin-top:15px;
              
          }
          #footer {
	background: #121d1f;
	color: #7d8384;
 text-align: center;
	padding: 30px 0 25px 0;
}
#footer p {
	font-size: 13px;
}
#footer a {
	color: #a0a5a5;
}
#footer a:hover {
	color: #7bc3d1;
         
      </style>
      
  </head>
  <body>
    
      <div class="container">
      
          <h1 style="color:white;">Weather Forecast</h1>
          
          
          
          <form>
  <fieldset class="form-group">
    <label for="city"><p style="color:white;">Enter the name of a city.</p></label>
    <input type="text" class="form-control" name="city" id="city" placeholder="Eg. Kearny, New York" value = "<?php 
																										   
																										   if (array_key_exists('city', $_GET)) {
																										   
																										   echo $_GET['city']; 
																										   
																										   }
																										   
																										   ?>">
  </fieldset>
  
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
      
          <div id="weather"><?php 
              
              if ($weather) {
                  
                  echo '<div class="alert alert-success" role="alert">
  '.$weather.'
</div>';
                  
              } else if ($error) {
                  
                  echo '<div class="alert alert-danger" role="alert">
  '.$error.'
</div>';
                  
              }
   
              
              ?></div>
      </div>
                 <div id="footer">
  
    
      <p> 2019 &copy; Sk Adib Asker</p>
	  
    
  
</div>

  
  </body>
</html>
