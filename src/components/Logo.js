import image from '../assets/logo.png';

function Logo() {
    return (
        <div>
            <img
                classNameZ=''
                src={image}
                alt='Logo'
                style={{width: '200px', height: 'auto'}}
            />
        </div>
    );
}

export default Logo;