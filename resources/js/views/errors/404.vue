<template>
  <div class="error-container">
    <div class="error-wrap">
      <h1 class="error-title">404</h1>
      <h4 class="error-subtitle">Sorry, but nothing exists here.</h4>
      <a href="/" class="error-button">Go Home</a>
    </div>

  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.error-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
  padding: 0;
  background-color: #e0e0e0;
}
.error-title{
  font-size: 150px;
}
.error-subtitle{
  margin-top: 40px;
  margin-bottom: 20px;
}
.error-button{
  background-color: #333386;
  padding: 10px;
  color: white;
  border-radius: 10px;
  cursor: pointer;
  text-decoration: none;
}
</style>