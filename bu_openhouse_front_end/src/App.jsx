import React, { useState } from 'react';
import Login from './Login';
import Register from './Register';
import Congratulation from './Congratulation';

function App() {
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    const handleLoginSuccess = () => {
        setIsAuthenticated(true);
    };

    const handleRegisterSuccess = () => {
        setIsAuthenticated(true);
    };

    return (
        <div>
            {!isAuthenticated ? (
                <>
                    <h2>Register</h2>
                    <Register onRegisterSuccess={handleRegisterSuccess} />
                    <h2>Login</h2>
                    <Login onLoginSuccess={handleLoginSuccess} />
                </>
            ) : (
                <Congratulation />
            )}
        </div>
    );
}

export default App;
