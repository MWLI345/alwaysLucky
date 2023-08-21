import "../css/Login.scss";

const Login = () => {
  return (
    <>
      <div className="banner">
        <h1>This is our banner!!!</h1>
      </div>
      <div className="login">
        <button>Click here to register</button>
        <button>Already have an account? Login here</button>
      </div>
      <div className="features">
        <div className="feature">
          <h3>feature 1</h3>
          <p>Wow look at this feature</p>
          <p>Description of feature. Wow!</p>
        </div>
        <div className="feature">
          <h3>feature 2</h3>
          <p>Wow look at this feature</p>
          <p>Description of feature. Wow!</p>
        </div>
        <div className="feature">
          <h3>feature 3</h3>
          <p>Wow look at this feature</p>
          <p>Description of feature. Wow!</p>
        </div>
      </div>
    </>
  );
};

export default Login;
