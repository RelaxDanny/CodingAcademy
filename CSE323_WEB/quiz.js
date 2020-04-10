// This allows the Javascript code inside this block to only run when the page
// has finished loading in the browser.

var recordCapital = []; // stores the capitals
var recordCountry = []; // stores the countries
var recordAnswer = [] ; // stores the answer
    
$( document ).ready(function() {  
  var country_capital_pairs = pairs
  $("#quiz-submit").click(function() {
    
    var correct = false;
    var wrong = false;
    var prevCapital = recordCapital[recordCapital.length - 1]; //the last element will be the prevCapital 
    
    var answer = document.getElementById("quiz-answer").value;
    recordAnswer.push(answer);

    prevCountry = document.getElementById("quiz-question").innerHTML;
    recordCountry.push(prevCountry);

    console.log("prevCountry : "+prevCountry);
    console.log("prevCaptial : "+prevCapital);

    if(answer == prevCapital){ //if correct,
      console.log("TRUE");
      insert_correct_table();
      // if($(".correct").hide()==true && $(".wrong").show() == true){
      if($("#wrong").is(":checked")){
        $("#all").prop("checked", true);
        $(".correct").show();
        $(".wrong").show();
      }
      if($("#correct").is(":checked")){
        $(".wrong").hide();
        $(".correct").show();
      }
    }
    else{
      console.log("FALSE");
      insert_wrong_table();
      //if($(".wrong").hide()==true && $(".correct").show() == true){
      if($("#correct").is(":checked")){
        $("#all").prop("checked", true);
        $(".correct").show();
        $(".wrong").show();
      } 
      if($("#wrong").is(":checked")){
        $(".wrong").show();
        $(".correct").hide();
      }
  
    }
    
    // console.log("Current Country is: " + prevCountry);
    //console.log("Current capital is: ", prevCapital);
    console.log("Current Answer is: " + answer);

    var x = Math.floor(Math.random() * pairs.length);

    var country = pairs[x].country;
    var capital = pairs[x].capital;
    
    recordCapital.push(capital); //keep pushing capitals to check the answer.

    document.getElementById("quiz-question").innerHTML = country; //A new, randomly selected question should be displayed.
    document.getElementById("quiz-answer").value = ""; //input should be cleared
    document.getElementById("quiz-answer").focus(); //input should get focus again.

    });
    var country_capital_pairs = pairs
    var x = Math.floor(Math.random() * pairs.length) + 1;
    var country = pairs[x].country;
    var capital = pairs[x].capital;
    recordCapital.push(capital);
    document.getElementById("quiz-answer").value = "";
    document.getElementById("quiz-question").innerHTML = country;
    document.getElementById("quiz-answer").focus();

    $("input:radio[id=all]").click(function(){
      console.log("filter = all");
      $(".correct").show();
      $(".wrong").show();
    });

    $("input:radio[id=correct]").click(function(){
      console.log("filter = correct");
      $(".wrong").hide();
      $(".correct").show();
    });

    $("input:radio[id=wrong]").click(function(){
      console.log("filter = wrong");
      $(".correct").hide();
      $(".wrong").show(); // . = class, # = id
    });  
});

function delete_w_row(){
  $('#wrong_filter').remove();
}
function delete_c_row(){
  $('#correct_filter').remove();

}
function insert_correct_table(){
  icon = document.getElementById('icon');
  $("#quiz-table tr:nth-child(3)").after("<tr name='filter', class='correct' id = 'correct_filter' style='color:blue;'><td>" + recordCountry[recordCountry.length - 1] + "</td>\
  <td>" + recordAnswer[recordAnswer.length - 1] + "</td>\
  <td>" + icon.innerHTML + "<input type = 'submit', id = 'quiz-delete', value = 'Delete', onclick = 'delete_c_row()'>"+"</td></tr>" + "<>");
  
}
function insert_wrong_table(){
  $("#quiz-table tr:nth-child(3)").after("<tr name='filter', class='wrong' id = 'wrong_filter' style='color:red;'><td>" + recordCountry[recordCountry.length - 1] + "</td>\
  <td><s>" +recordAnswer[recordAnswer.length - 1] + "</s></td>\
  <td>" + recordCapital[recordAnswer.length - 1] + "<input type = 'submit', class = 'quiz-delete', id = 'quiz-delete', value = 'Delete', onclick = 'delete_w_row()'>"+"</td></tr>");

}

