$(document).ready(function (){
    var count = 0;

    $('.total-form').append('<input type="Course Name" placeholder="Enter Course Name" name="courseName"></input> <input type = "Credit Hours" placeholder = "Enter Credit Hours" id="creditHr' +count+ '" name="creditHr"></input>
<select name="grade" id="grade'+count+'"required><option value="">Letter Grade</option><option value="4.0">A+</option><option value="3.667">A-</option><option value="3.333">B+</option><option value="3.0">B</option><option value="2.667">B-</option>
                <option value="2.333">C+</option>
                <option value="2.000">C</option>
                <option value="1.667">C-</option>
                <option value="1.333">D+</option>
                <option value="1.0">D</option>
                <option value="0.667">D-</option>
                <option value="0.0">F</option>
             </select>
            <button type="button" class="add-gpa-row"><i class="fa fa-plus-circle"></i></button>
      </div>');
    count++;
});