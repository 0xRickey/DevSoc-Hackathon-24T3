import { Box, Typography } from '@mui/material';
function Footer() {
    return (
        <Box
            sx={{
                width: '100%',
                backgroudColor: '#f5f5f5',
                textAlign: 'center',
                padding: '10px 0',
                bottom: '0',
                left: '0'
            }}
        >
            <Typography variant="standard" color="black">
                @Team 3 2024
            </Typography>
        </Box>  
    );
}

export default Footer;