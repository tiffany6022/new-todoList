<template lang="pug">
#taskdetails
  textarea(v-model="content")
  li {{item.title}}
</template>


<script>
  export default{

    data(){
      return{
        content: "",
      }
    },

    props: ['item']

  }
</script>


<style lang="sass">
  #taskdetails
    textarea
      width: 30vw
      height: 10vw
      margin-bottom: 1vw
</style>



