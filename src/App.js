import './App.css';
import CourseRating from './components/CourseRating.js';
import Logo from './components/Logo.js';
import Footer from './components/Footer.js';
import React, { useState } from 'react';
import { CardContent, CardHeader, Card, Typography, Autocomplete, TextField, Stack, Button, Box, Container, CircularProgress } from '@mui/material';

import { getElectiveCourses, getCoreCourses, getSatisfiedPrereqq , getAllCourses } from './getData/dataFetch.js';

function App() {
  const [selectedDegree, setSelectedDegree] = useState('');
  const handleDegree = (event, value) => {
    setSelectedDegree(value);
  }

  const [selectedMajor, setSelectedMajor] = useState('');
  const handleMajor = (event, value) => {
    setSelectedMajor(value);
  }

  const [isLoading, setIsLoading] = useState(false);
  const [selectedCourses, setSelectedCourses] = useState([]);

  const [isOpen, setIsOpen] = useState(false);

  const fetchData = () => {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve();
      }, 500);
    });
  };
  
  const handleButtonClick = async () => {
    setIsLoading(true);
    setIsOpen(true);

     // Simulate data fetching (replace this with your actual fetching logic)
    try {
      // Call your data fetching functions here
      await fetchData(); // Replace this with your actual fetching function

      // You can also set selected courses or other state here based on the fetched data
    } catch (error) {
      console.error("Error fetching data:", error);
      // Handle error accordingly (optional)
    } finally {
      setIsLoading(false); // Stop loading after fetching is complete
    }

    // const jsonData = JSON.stringify(selectedMajor, null, 2);
    // const blob = new Blob([jsonData], { type: 'application/json' });
    // const link = document.createElement('a');
    // link.href = URL.createObjectURL(blob); 
    // link.download = 'data.json';
    // document.body.appendChild(link);
    // link.click();
    // document.body.removeChild(link);
  };

  

  const degreeProps = {
    options: degrees.map((option) => option.name),
  };

  const majorProps = {
    options: majors.map((option) => option.name),
  };

  const handleClick = (url) => {
    window.open(url, '_blank');
  };

  return (
    <body>
      <div style={{ textAlign: 'center', margin: '20px 0' }}>
        <Logo/>
      </div>
      <Typography variant="h1" fontWeight="bold" gutterBottom align="center" color="#7f4d3e">CoursEz</Typography>
      <Stack spacing={4}>
        <Autocomplete
          {...degreeProps}
          id="flat-demo"
          renderInput={(params) => (
            <TextField {...params} label="Your degree~" variant="standard" />
          )}
          onChange={handleDegree}
        />

        <Autocomplete
          {...majorProps}
          id="flat-demo"
          renderInput={(params) => (
            <TextField {...params} label="Your major~" variant="standard" />
          )}
          onChange={handleMajor}
        />
{/* 
        <Autocomplete
          multiple
          id="tags-standard"
          options={courses}
          getOptionLabel={(option) => option.name}
          onChange={(event, newValue) => {
            setSelectedCourses(newValue);
          }}
          renderInput={(params) => (
            <TextField
              {...params}
              variant="standard"
              label="Courses you've done so far~"
            />
          )}
        /> */}


          <Container>
            <Box sx={{ 
              display: 'flex', 
              justifyContent: 'center',
              mt: 1
          }}>
        <Button onClick={handleButtonClick} variant="outlined" color="sucess"  disabled={isLoading}>
          {isLoading ? 'Loading...' : 'Fetching Data~'}
          
        </Button>
        
        {isLoading && <CircularProgress sx={{ marginLeft: 1 }} />}
          </Box>
          </Container>
          <div>
          {isOpen && (
            <Box sx={{ display: 'flex', justifyContent: 'space-around', marginTop: 2 }}>
              {/* Core Courses Card */}
              <Card sx={{ width: '45%' }}>
                <CardHeader title="Core Courses" sx={{ backgroundColor: '#a66c5a', color: '#f7f0eb'}} />
                <CardContent>
                  {getCoreCourses(selectedMajor, "1").map((item, index) => (
                    <Box key={index} sx={{ display: 'flex', alignItems: 'center', marginBottom: 2 }}>
                      <Typography 
                        key={index} 
                        onClick={() => handleClick(item.handbookUrl)} 
                        style={{ cursor: 'pointer', color: '#7f4d3e', marginRight: 40 }} 
                        variant="body1"
                      >
                        {item.code}
                      </Typography>
                      
                      <CourseRating score={item.rating || 0} />
                    </Box>
              
                  ))}
                  
                </CardContent>
              </Card>

              {/* Elective Courses Card */}
              <Card sx={{ width: '45%' }}>
                <CardHeader title="Elective Courses" sx={{ backgroundColor: '#a66c5a', color: '#f7f0eb' }} />
                <CardContent>
                  {getElectiveCourses(selectedMajor, "2").map((item, index) => (
                    <Box key={index} sx={{ display: 'flex', alignItems: 'center', marginBottom: 2 }}>
                      <Typography 
                        onClick={() => handleClick(item.handbookUrl)} 
                        style={{ cursor: 'pointer', color: '#7f4d3e', marginRight: 40 }} 
                        variant="body1"
                      >
                        {item.code}
                      </Typography>
                      
                      <CourseRating score={item.rating || 0} />
                    </Box>
                  ))}
                </CardContent>
              </Card>
            </Box>
          )}
        </div>

          <div >
        
        
          {isOpen && (
            <div style={{ display: 'flex', justifyContent: 'space-around', marginTop: '20px' }}>
              
              {/* Term 1 Card */}
              <Card sx={{ width: '30%' }}>
                <CardHeader 
                  title="Term 1" 
                  sx={{ 
                    backgroundColor: '#f9ece3', // Change this color to your desired background color
                    color: '#7f4d3e' // Change text color if needed
                  }} 
                />
                <CardContent>
                  {getSatisfiedPrereqq(selectedMajor, "1").map((item, index) => (
                    <Typography 
                      key={index} 
                      onClick={() => handleClick(item.handbookUrl)} 
                      style={{ cursor: 'pointer', color: '#7f4d3e' }} 
                      variant="body1"
                    >
                      {item.code}
                    </Typography>
                  ))}
                </CardContent>
              </Card>

              {/* Term 2 Card */}
              <Card sx={{ width: '30%' }}>
                <CardHeader 
                  title="Term 2" 
                  sx={{ 
                    backgroundColor: '#eddbce', // Change this color to your desired background color
                    color: '#7f4d3e' // Change text color if needed
                  }} 
                />
                <CardContent>
                  {getSatisfiedPrereqq(selectedMajor, "2").map((item, index) => (
                    <Typography 
                      key={index} 
                      onClick={() => handleClick(item.handbookUrl)} 
                      style={{ cursor: 'pointer', color: '#7f4d3e' }} 
                      variant="body1"
                    >
                      {item.code}
                    </Typography>
                  ))}
                </CardContent>
              </Card>

              {/* Term 3 Card */}
              <Card sx={{ width: '30%' }}>
                <CardHeader 
                  title="Term 3" 
                  sx={{ 
                    backgroundColor: '#ebd1c0', // Change this color to your desired background color
                    color: '#7f4d3e' // Change text color if needed
                  }} 
                />
                <CardContent>
                  {getSatisfiedPrereqq(selectedMajor, "3").map((item, index) => (
                    <Typography 
                      key={index} 
                      onClick={() => handleClick(item.handbookUrl)} 
                      style={{ cursor: 'pointer', color: '#7f4d3e' }} 
                      variant="body1"
                    >
                      {item.code}
                    </Typography>
                  ))}
                </CardContent>
              </Card>

            </div>
          )}
          <Footer />
        </div>
        
      </Stack>
    </body>
    
  );
}

const degrees = [
  {name: "Computer science"},
]

const majors = [
  {name: "Computer Science"},
  {name: "Database Systems"},
  {name: "Artificial Intelligence"},
  {name: "Programming Languages"},
  {name: "Computer Networks"},
  {name: "Embedded Systems"},
  {name: "Security Engineering"},
]

const courses = getAllCourses();

export default App;
