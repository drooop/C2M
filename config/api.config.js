const isPro = Object.is(process.env.NODE_ENV, "production");

console.log(isPro);

module.exports = {
  baseUrl: isPro ? "http://127.0.0.1/api" : "http://127.0.0.1/api"
};
