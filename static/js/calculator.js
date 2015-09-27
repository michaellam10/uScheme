$(document).ready(function() {

    //var courseName = $(#course-name).val()
    $('#gradeForm').submit(function() {
        var $inputs = $('#course-name :input');

        var values = {};
        $inputs.each(function() {
            values[this.name] = $(this).val();
        });
    });

});