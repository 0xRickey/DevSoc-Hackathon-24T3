import * as React from 'react';
import { Rating, Box} from '@mui/material';
import StarIcon from '@mui/icons-material/Star';
function CourseRating({ score }) {
    const labels = {
        2: 'Ok',
        3: 'Good',
        4: 'Excellent',
        5: 'Excellent+',

    };

    return (
        <Box sx={{width: 200, display: 'flex', alignItems: 'center'}}>
            <Rating
                className="course-rating"
                value={score}
                readOnly
                precision={0.5}
                emptyIcon={<StarIcon sytle={{ opacity: 0.55}} fontSize="inherit"/>}
            />
            <Box sx={{ ml: 4 }}>{labels[Math.ceil(score)] || 'No Rating'}</Box>
        </Box>
    );
}

export default CourseRating