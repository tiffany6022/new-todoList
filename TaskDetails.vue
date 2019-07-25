<template lang="pug">
#taskdetails
  textarea(v-model="content")
</template>


<script>
  export default{

    data(){
      return{
        content: "",
      }
    },

  }
</script>


<style lang="sass">
  #taskdetails
    textarea
      width: 30vw
      height: 10vw
      margin-bottom: 1vw
</style>



