import Card from "./Card";

import type { Employee } from "../types/employee";

interface EmployeeCardProps {
    employee: Employee;
    onView : (employee : Employee) => void;
}

export  default function EmployeeCard({
    employee,
    onView
}: EmployeeCardProps) {
    return (
        <Card title={employee.name} >
            <p>
                <strong>Role:</strong> {employee.role}
            </p>

            <p>
                <strong>Department:</strong> {employee.department}
            </p>

            <p style={{color: employee.isActive ? "green" : "red",}}>
                {employee.isActive ? "Active" : "Inactive"}
            </p>

            <button  onClick={() => onView(employee)}> 
                View Details
            </button>
        </Card>
    );
}

