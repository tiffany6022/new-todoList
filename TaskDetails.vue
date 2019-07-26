<template lang="pug">
#taskdetails
  textarea(v-model="item.content", :keyup="$emit('item')")
  li {{item.title}}
</template>


<script>
  export default{

    data(){
      return{
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



