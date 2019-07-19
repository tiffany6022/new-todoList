<template lang="pug">
#app
  .ui.action.input
    input(type="text", v-model="todo")
    button.ui.icon.button(@click="addTask(todo)")
      i.plus.icon

  .ui.checkbox(v-for="task in tasks")
    input(type="checkbox", :id="task.title", @click="toggle(task)")
    label(:for="task.title", v-if="task.done")
      del {{ task.title }}
      i.close.icon(@click="deleteTask(task)")
    label(:for="task.title", v-else) {{ task.title }}
</template>


<script>
  export default{
    data(){
      return{
        todo: "abc",
        tasks: []
      }
    },
    methods: {
      addTask: function(tsk){
        if(tsk){
          this.tasks.push({
            title: tsk,
            done: false
          });
          this.todo = "";
        }
      },
      toggle: function(tsk){
        console.log(this.tasks.indexOf(tsk));
        console.log("toggle");
        if(tsk.done){
          tsk.done = false;
        }
        else{
          tsk.done = true;
        }
      },
      deleteTask: function(tsk){
        //console.log(this.tasks.indexOf(tsk));
        this.tasks.splice(this.tasks.indexOf(tsk), 1);
        //console.log(this.tasks.indexOf(tsk));
      },
    },
  }
</script>


<style lang="sass">

</style>
