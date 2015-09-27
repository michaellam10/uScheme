$(document).ready(function (){
    var $result= $('#grade');
    var totalGradePoint = 0;

    $('#myForm').submit(function() {
    // get all the inputs into an array.
    var $inputs = $('#myForm :input');

    // not sure if you wanted this, but I thought I'd add it.
    // get an associative array of just the values.
    var values = {};
    $inputs.each(function() {
        values[this.name] = $(this).val();
    });

    });

    var totalCreditPoint += creditHours;
    var gpaCalc(function(creditHours, grade) {
        var gradeNum = 0.00;
        if (grade === 'A') {
            gradeNum = 4.00;
        } else if (grade === 'A-') {
            gradeNum = 3.67;
        } else if (grade === 'B+') {
            gradeNum = 3.33;
        } else if (grade === 'B') {
            gradeNum = 3.00;
        } else if (grade === 'B-') {
            gradeNum = 2.67;
        } else if (grade === 'C+') {
            gradeNum = 2.33;
        } else if (grade === 'C') {
            gradeNum = 2.00;
        } else if (grade === 'C-') {
            gradeNum = 1.67;
        } else if (grade === 'D+') {
            gradeNum = 1.33;
        } else if (grade === 'D') {
            gradeNum = 1.00;
        } else if (grade === 'D-') {
            gradeNum = 0.67;
        } 

        return gradeNum * creditHours;
    })
    totalGradePoint += gpaCalc('#credit', '#grade');
    var finalGpa = totalGradePoint / totalCreditPoint;

});
