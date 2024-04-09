from redbird.repos import MemoryRepo
from rocketry import Rocketry
from rocketry.conds import secondly

rockApp = Rocketry(logger_repo=MemoryRepo()
                   , config={
        'task_execution': 'process',
        'task_pre_exist': 'raise',
        'force_status_from_logs': True,

        'silence_task_prerun': False,
        'silence_task_logging': False,
        'silence_cond_check': False,

        'max_process_count': 5,
        'restarting': 'replace',
        'cycle_sleep': 0.1
    })


class SchedulerService:
    pass


def trigger_scheduler():
    rockApp.run()


@rockApp.task(secondly)
def do_main():
    print("Scheduler is running")
