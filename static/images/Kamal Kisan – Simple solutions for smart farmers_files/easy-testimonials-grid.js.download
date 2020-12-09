var easy_testimonials_grid_resize_timer;
var easy_testimonials_grid_resize_rows = function ()
{
	// find the tallest testimonial in each row, and set all the other heights to match it
	var rows = jQuery('.easy_testimonials_grid_equal_height_rows > .easy_testimonials_grid_row');
	rows.each(function (row_index) {
		var max_height = 0;
		var bodies = jQuery(this).find('.easy_testimonials_grid_cell .testimonial_body');
		
		// reset all testimonials to their natural height, to allow for accurate comparison
		bodies.css('min-height', 'initial');
		
		// find the tallest one
		bodies.each(function () {
			var my_height = jQuery(this).height();
			if (my_height > max_height) {
				max_height = my_height;
			}
		});
		
		// set all testimonials to be the same height as the tallest one
		if (max_height > 0) {
			bodies.css('min-height', max_height);
		}
		
	});		
};

jQuery( function () {
	if ( jQuery('.easy_testimonials_grid_equal_height_rows').length > 0 ) {
		easy_testimonials_grid_resize_rows();
		jQuery(window).resize( function () {
			clearTimeout(easy_testimonials_grid_resize_timer);
			easy_testimonials_grid_resize_timer = setTimeout(easy_testimonials_grid_resize_rows, 100);
		} );
	}
});