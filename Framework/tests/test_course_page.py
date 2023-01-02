import pytest


@pytest.mark.smoke
def test_play_video(open_course_page):
    course = open_course_page.play_video()
    assert course.is_video_start() is True


@pytest.mark.skip('Skipped test')
@pytest.mark.regression
def test_open_curriculum_about_course(scroll_course_page):
    course = scroll_course_page.open_info_section()
    assert course.title_value() == "Introduction"


@pytest.mark.skip('Skipped test')
@pytest.mark.regression
def test_mentor_info(scroll_course_page_to_end):
    info = scroll_course_page_to_end
    assert info.is_email_is_present() is True


@pytest.mark.skip('Skipped test')
@pytest.mark.smoke
def test_start_course(scroll_course_page_to_middle):
    course = scroll_course_page_to_middle.start_course()
    assert course.is_course_name_displayed() is True
