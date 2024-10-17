import './App.css';
import React, { useState } from 'react';
import { Typography, Autocomplete, TextField, Stack, Button, Box, Container, CircularProgress } from '@mui/material';

import { getSatisfiedPrereq, getSatisfiedPrereqq , getAllCourses } from './getData/dataFetch.js';

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

  const handleButtonClick = () => {
    setIsOpen(true);

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
      <Typography variant="h1" fontWeight="bold" gutterBottom align="center" color="black">Somthing</Typography>
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


        {isLoading && <CircularProgress />}
        


            </Box>
          </Container>
          <div >
        
        
          {isOpen && (
              <div style={{ display: 'flex', justifyContent: 'space-around' }}>
                <div> 
                <h2>Term1</h2>
                {getSatisfiedPrereqq(selectedMajor, "1").map((item, index)=>(
                //{getSatisfiedPrereq(selectedMajor, "1", selectedCourses).map((item, index)=>(
                   <p key={index} onClick={() => handleClick(item.handbookUrl)} style={{ cursor: 'pointer', color: 'grey' }}>
                   {item.code}
                 </p>
                ))}
                </div>

                <div> 
                <h2>Term2</h2>
                //{getSatisfiedPrereqq(selectedMajor, "2").map((item, index)=>(
                //{getSatisfiedPrereq(selectedMajor, "2", selectedCourses).map((item, index)=>(
                   <p key={index} onClick={() => handleClick(item.handbookUrl)} style={{ cursor: 'pointer', color: 'grey' }}>
                   {item.code}
                 </p>
                ))}
                </div>

                <div> 
                <h2>Term3</h2>
                {getSatisfiedPrereqq(selectedMajor, "3").map((item, index)=>(
                //{getSatisfiedPrereq(selectedMajor, "3", selectedCourses).map((item, index)=>(
                   <p key={index} onClick={() => handleClick(item.handbookUrl)} style={{ cursor: 'pointer', color: 'grey' }}>
                   {item.code}
                 </p>
                ))}
                </div>
              </div>
          )}
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
