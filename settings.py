css = """
h1 {
  font-size: 72px;
  background: -webkit-linear-gradient(#FF0000, #8B0000);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

#api-form {
    width: 100%;
    margin: auto;
}

#snow-container {
    position: relative;
    width: 100%;
    height: 150px;
    overflow: hidden;
}

@keyframes snow {
    0% { transform: translateY(0); }
    100% { transform: translateY(100vh); }
}

.snowflake {
    position: absolute;
    top: -10px;
    background: white;
    border-radius: 50%;
    opacity: 0.8;
    animation: snow 10s linear infinite;
}

.snowflake:nth-child(odd) {
    width: 10px;
    height: 10px;
    left: calc(100% * var(--i) / 10);
    animation-duration: calc(5s + var(--i) * 1s);
}

.snowflake:nth-child(even) {
    width: 5px;
    height: 5px;
    left: calc(100% * var(--i) / 10);
    animation-duration: calc(7s + var(--i) * 1s);
}
"""